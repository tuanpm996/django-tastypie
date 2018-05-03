from tastypie.resources import ModelResource
from actions.models import *
from tastypie.authorization import Authorization
import json
from tastypie_mongoengine import fields 
from tastypie_mongoengine import resources 
import datetime
from django.http import JsonResponse

deal_action_list = ["user_view_deal", "user_search_deal", "user_save_deal"]
coupon_action_list = ["user_start_get_coupon", "user_get_coupon_success"]
brand_action_list = ["user_view_brand", "user_follow_brand"]

class ActionResource(resources.MongoEngineResource):
    class Meta:
        queryset = Action.objects.all()
        resource_name = 'action'
        allowed_methods = ['get', 'post']
        authorization = Authorization()

    def dehydrate_action(self, bundle):
        # import pdb; pdb.set_trace()
        return json.loads(bundle.data['action'])

    # def obj_get(self, bundle, **kwargs):
    #     import pdb ; pdb.set_trace()

    def obj_create(self, bundle, **kwargs):
        action_type = ActionType.objects(action_name=bundle.data['action'])
        new_action = None
        action_name = action_type[0].action_name #exception

        import pdb; pdb.set_trace()
        if action_name in deal_action_list:
            new_action = DealAction(
                url = bundle.data['url'],
                action = action_type[0],
                time = datetime.datetime.now(),
                title = bundle.data['title'], #exception
                ip  = bundle.request.META.get('HTTP_X_FORWARDED_FOR'), #exception
                agent = bundle.request.META.get('HTTP_USER_AGENT'), #exception
                referer = bundle.request.META.get('HTTP_REFERER'), #exception 
                deal_id = bundle.data['deal_id'] #exception
            )
        elif action_name in coupon_action_list:
            new_action = CouponAction(
                url = bundle.data['url'],
                action = action_type[0],
                time = datetime.datetime.now(),
                title = bundle.data['title'],
                ip  = bundle.request.META.get('HTTP_X_FORWARDED_FOR'),
                agent = bundle.request.META.get('HTTP_USER_AGENT'),
                referer = bundle.request.META.get('HTTP_REFERER'),
                coupon_id = bundle.data['coupon_id']
            )
        elif action_name in brand_action_list:
            new_action = BrandAction(
                url = bundle.data['url'],
                action = action_type[0],
                time = datetime.datetime.now(),
                title = bundle.data['title'],
                ip  = bundle.request.META.get('HTTP_X_FORWARDED_FOR'),
                agent = bundle.request.META.get('HTTP_USER_AGENT'),
                referer = bundle.request.META.get('HTTP_REFERER'),
                brand_id = bundle.data['brand_id']
            )

        import pdb; pdb.set_trace()
        new_action.save() 
        return new_action

class ActionTypeResource(resources.MongoEngineResource):
    class Meta:
        queryset = ActionType.objects.all()
        allowed_methods = ['get']
        resource_name = 'actionType'
        authorization = Authorization()

class DealActionResource(resources.MongoEngineResource):
    class Meta:
        queryset = DealAction.objects.all()
        resource_name = 'dealAction'

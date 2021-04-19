from flask_restful import Api, Resource, reqparse

class HelloApiHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message' : 'Hello Api Handler'
        }
    
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_Argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.aprse_args()

        print(args)

        request_type = args['type']
        request_json = args['message']

        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = "Your Message Requested: {}".format(ret_msg)
        else:
            message = "no Msg"
        
        final_ret = {"status": "Success", "message": message}

        return final_ret
        
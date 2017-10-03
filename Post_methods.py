from crud_csv import save_csv, read_csv

class Post:
		def __init__(self, post_id):
			self.post_id = post_id

		def show_all_post(self, user_id):
			'''
			The method shows all the saved posts

			:rtype: dictionary
			:param: post_id, user_id  
			:return: a dictionary of all post
			'''

			self.user_id

			## get data from save source and return the data

		def create_post(self, post_id, user_id, body, created_at, updated_at = ''):
			'''
			The method allows you to create a post

			:rtype: dictionary
			:param post_id, user_id, body, created at
			:return: a dictionary with the post attributes to be cresated
			'''

			self.post_id = post_id
			self.user_id = user_id
			self.body = body
			self.created_at = created_at
			self.updated_at = updated_at
			save_post = {"post_id":post_id, "user_id":user_id, "body":body, "created_at":created_at, "updated_at": updated_at}
			return save_post


		def edit_post(self, post_id, user_id, updated_at):

			'''
			The method allows you to update a post

			:rtype: dictionary
			:param post_id, user_id, body, updated_at
			:return: a dictionary with the attributed to be updated
			'''
			
			self.post_id = post_id
			self.user_id = user_id
			self.updated_at = updated_at
			upadte_post = {"post_id":post_id, "user_id":user_id, "updated_at":updated_at}
			return updated_post


		def delete_post(self, post_id, user_id):
			'''
			The Method helps you to delete a post

			:rtype: dictionary
			:param post_id, user_id
			:return: a dictionary with the id of the user and post
			'''
			self.post_id = post_id
			self.user_id = user_id
			
			#send to the delete method
			remove_post = {"post_id":post_id, "user_id":user_id}

		def share(self, post_id, user_id, share = []):
			'''
			The method allows users  to share post 

			:rtype: list
			:param post_id, user_id
			:return: the list of users who shared the post
			'''

			self.post_id = post_id
			self.user_id = user_id
			self.share = share.append(user_id)
			return share


		def like(self, post_id, user_id, like = []):
			'''
			The method allows users to like post 

			:rtype: list
			:param post_id, user_id
			:return: the list of users who like the post
			'''

			self.post_id = post_id
			self.user_id = user_id
			self.like = like.append(user_id)
			return like
			





post = Post(1)
save_post = post.create_post(1, 1, "My First Blog Post", "2nd October 2017")



"""file_name = "posts.csv" 
fieldnames = ['post_id', 'user_id', 'body', 'created_at', 'updated_at'] 
dictionary = save_post
save_csv(file_name, fieldnames, save_post)"""

file_name = "posts.csv"
read_csv(file_name)












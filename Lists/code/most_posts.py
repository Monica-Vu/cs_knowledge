posts = [
    { "author": "jasonle", "content": "I eat potatoes!" },
    { "author": "boo", "content": "Boo is beautiful!"},
    { "author": "jasonle", "content": "I think my boo is amazing!"}
]

posts_tie = [
	{ "author": "boo", "content": "Boo is beautiful!"},
    { "author": "jasonle", "content": "I eat potatoes!" },
    { "author": "jasonle", "content": "I think my boo is amazing!"},
	{ "author": "boo", "content": "My boo is beautiful too!"},
]

posts_three = [
	{ "author": "matt", "content": "I am beautiful!"},
	{ "author": "boo", "content": "Boo is beautiful!"},
    { "author": "jasonle", "content": "I eat potatoes!" },
    { "author": "jasonle", "content": "I think my boo is amazing!"},
	{ "author": "boo", "content": "My boo is beautiful too!"},
	{ "author": "jasonle", "content": "I work at Unity!"},
]

def find_num_posts_per_author(posts):
	posts_dict = {}

	for i in range(len(posts)):
		if posts[i]["author"] in posts_dict.keys():
			posts_dict[posts[i]["author"]] += 1
		else: 
			posts_dict[posts[i]["author"]] = 1

	return posts_dict 

def find_top_poster(posts_dict):
	max_num_posts = 0
	top_poster = ""

	for key, value in posts_dict.items(): 
		if value > max_num_posts:
			max_num_posts = value 
			top_poster = key 
	
	return top_poster

def solution(posts):
	posts_dict = find_num_posts_per_author(posts)
	return find_top_poster(posts_dict)

print(solution([]))	# ""
print(solution(posts))	# jasonle
print(solution(posts_tie))	# boo
print(solution(posts_three))	# jasonle
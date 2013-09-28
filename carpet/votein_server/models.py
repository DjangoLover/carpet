from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class Vote(models.Model):
	voter_ID = models.CharField(max_length=50)		#can be external like Facebook ID
	DOWN = 'Dw'
	UP = 'Up'
	VOTE_CHOICES = (
		(DOWN, 'Down'),
		(UP, 'Up'),
	)
	voteType = models.CharField(max_length=2,
                                      choices=VOTE_CHOICES,
                                      default=UP)
	def __unicode__(self):
		return self.voteType in (self.UP, self.DOWN)

# Used by Article class
class Image(models.Model):
	submitter = models.CharField(max_length=50)
	imageURL = models.URLField();					#Do we need images as opinions, like an artist's work etc?
	def __unicode__(self):							#Also, Consider changing this to FileField
		return self.imageURL

#Used by Opinion and Comment classes
class totalVotes(models.Model):
	upVotes = models.ManyToManyField(Vote)
	downVotes = models.ManyToManyField(Vote)
	def __unicode__(self):
		return self.id

###########################################################################
######					Main Class Models  								###
###########################################################################

# Used by Article class
class Comment(models.Model):
	commentText = models.CharField(max_length=1000)
	commentVotes = models.ManyToManyField(totalVotes)
	submitter = models.CharField(max_length=50)
	def __unicode__(self):
		return self.commentText
	def AddVote(self, vote):
		if vote.voteType == Vote.VOTE_CHOICES.Up:
			self.commentVotes.upVotes.add(vote) 
		else if vote.voteType == Vote.VOTE_CHOICES.Down:
			self.commentVotes.downVotes.add(vote)
		self.save()

# Used by the Article class
class Opinion(models.Model):
	opinionText = models.CharField(max_length=1000)
	submitter = models.CharField(max_length=50)
	opinionComment = models.ManyToManyField(Comment)
	opinionVotes = models.ManyToManyField(totalVotes)
	def __unicode__(self):
		return self.opinionText
	def addComment(self, comment):
		self.comment.add(comment)
	def AddVote(self, vote):
		if vote.voteType == Vote.VOTE_CHOICES.Up:
			self.opinionVotes.upVotes.add(vote) 
		else if vote.voteType == Vote.VOTE_CHOICES.Down:
			self.opinionVotes.downVotes.add(vote)
		self.save()

class Article(models.Model):
	articleName = models.CharField(max_length=100)
	submitter = models.CharField(max_length=50)
	articeOpinion = ManyToManyField(Opinion)
	articleComments = ManyToManyField(Comments)
	articleVotes = OneToOneField(totalVotes)
	def __unicode__(self):
		return self.name
	def addComment(self, comment):
		self.comment.add(comment)
	def AddVote(self, vote):
		if vote.voteType == Vote.VOTE_CHOICES.Up:
			self.articleVotes.upVotes.add(vote) 
		else if vote.voteType == Vote.VOTE_CHOICES.Down:
			self.articleVotes.downVotes.add(vote)
		self.save()

def getArticleUpVotes(obj):
	try:
		art = Article.objects.get(obj = obj)
		return art.articleVotes.upVotes.count()
	except ObjectDoesNotExist:
		print "Object does not exist"

def getArticleDownVotes(obj):
	try:
		art = Article.objects.get(obj = obj)
		return art.articleVotes.downVotes.count()
	except ObjectDoesNotExist:
		print "Object does not exist"

def getOpinionUpVotes(obj):
	try:
		op = opinion.objects.get(obj = obj)
		return op.opinionVotes.upVotes.count()
	except ObjectDoesNotExist:
		print "Object does not exist"

def getOpinionDownVotes(obj):
	try:
		op = Opinion.objects.get(obj = obj)
		return op.opinionVotes.downVotes.count()
	except ObjectDoesNotExist:
		print "Object does not exist"


def getCommentUpVotes(obj):
	try:
		cmt = Comment.objects.get(obj = obj)
		return cmt.commentVotes.upVotes.count()
	except ObjectDoesNotExist:
		print "Object does not exist"

def getOpinionDownVotes(obj):
	try:
		cmt = Comments.objects.get(obj = obj)
		return cmt.commentVotes.downVotes.count()
	except ObjectDoesNotExist:
		print "Object does not exist"
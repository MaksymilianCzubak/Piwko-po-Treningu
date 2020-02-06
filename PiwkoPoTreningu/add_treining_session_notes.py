'''class TrainingSessionNotes(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    training_notes = models.TextField()
    training_session = models.ForeignKey(TrainingSession, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    user_weight = models.FloatField()
    user_vo2max = models.FloatField()'''

from PortalTreningowy.models import User, TrainingSession, TrainingSessionNotes

tsn= TrainingSessionNotes.objects.create(user=User(pk=1), training_notes='Było wspaniale',
                                        training_session=TrainingSession(pk=1),user_weight=90.5, user_vo2max=40.5)
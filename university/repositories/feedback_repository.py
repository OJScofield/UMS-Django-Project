from university.models import Feedback

class FeedbackRepository:

    @staticmethod
    def get_all_feedbacks():
        return Feedback.objects.all()

    @staticmethod
    def get_feedback_by_id(feedback_id):
        return Feedback.objects.get(pk=feedback_id)

    @staticmethod
    def create_feedback(feedback_data):
        feedback = Feedback(**feedback_data)
        feedback.save()
        return feedback

    @staticmethod
    def update_feedback(feedback_id, **kwargs):
        feedback = Feedback.objects.get(pk=feedback_id)
        for key, value in kwargs.items():
            setattr(feedback, key, value)
        feedback.save()
        return feedback

    @staticmethod
    def delete_feedback(feedback):
        feedback.delete()

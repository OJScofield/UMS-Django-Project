from university.exceptions import ResourceException, DatabaseException
from university.models import Feedback
from university.repositories import FeedbackRepository

class FeedbackComponent:

    def get_all_feedbacks(self):
        return FeedbackRepository.get_all_feedbacks()

    def get_feedback_by_id(self, feedback_id):
        try:
            return FeedbackRepository.get_feedback_by_id(feedback_id)
        except Feedback.DoesNotExist:
            raise ResourceException(f"Feedback with id {feedback_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error retrieving feedback with id {feedback_id}: {str(e)}")

    def create_feedback(self, feedback_data):
        try:
            return FeedbackRepository.create_feedback(feedback_data)
        except Exception as e:
            raise DatabaseException(f"Error creating feedback: {str(e)}")

    def update_feedback_by_id(self, feedback_id, data):
        try:
            feedback = FeedbackRepository.get_feedback_by_id(feedback_id)
            FeedbackRepository.update_feedback(feedback_id, **data)
        except Feedback.DoesNotExist:
            raise ResourceException(f"Feedback with id {feedback_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error updating feedback with id {feedback_id}: {str(e)}")

    def delete_feedback_by_id(self, feedback_id):
        try:
            feedback = FeedbackRepository.get_feedback_by_id(feedback_id)
            FeedbackRepository.delete_feedback(feedback)
        except Feedback.DoesNotExist:
            raise ResourceException(f"Feedback with id {feedback_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error deleting feedback with id {feedback_id}: {str(e)}")
        return True

from django.contrib.auth.tokens import PasswordResetTokenGenerator
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f"{user.is_active}{user.pk}{timestamp}"
    
generate_token = TokenGenerator()
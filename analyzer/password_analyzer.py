from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    return {
        'password': password,
        'score': result['score'],  # Score: 0 (weak) to 4 (strong)
        'feedback': result['feedback']
    }

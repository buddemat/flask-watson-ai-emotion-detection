import unittest
from EmotionDetection.emotion_detection import run_watson_emotion_detection as emo

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result = emo('I am glad this happened')
        self.assertEqual(result.get('dominant_emotion'), 'joy')
        result = emo('I am really mad about this')
        self.assertEqual(result.get('dominant_emotion'), 'anger')
        result = emo('I feel disgusted just hearing about this')
        self.assertEqual(result.get('dominant_emotion'), 'disgust')
        result = emo('I am so sad about this')
        self.assertEqual(result.get('dominant_emotion'), 'sadness')
        result = emo('I am really afraid that this will happen')
        self.assertEqual(result.get('dominant_emotion'), 'fear')

unittest.main()
import json
import watson_developer_cloud.VisualInsightsV1Experimental as VisualInsights


visual_insights = VisualInsights(username='YOUR SERVICE USERNAME',
                                 password='YOUR SERVICE PASSWORD')

print(json.dumps(visual_insights.classifiers(), indent=2))

with open('../resources/images.zip', 'rb') as images_file:
    print(json.dumps(visual_insights.summary(images_file), indent=2))

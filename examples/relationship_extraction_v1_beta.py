import watson_developer_cloud.RelationshipExtractionV1Beta as RelationshipExtraction


relationship_extraction = RelationshipExtraction(username='YOUR SERVICE USERNAME',
                                                 password='YOUR SERVICE PASSWORD')

print(relationship_extraction.extract("Hello from IBM Watson"))

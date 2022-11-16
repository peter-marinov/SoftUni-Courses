from static_and_class_methods_exercise.document_management.category import Category
from static_and_class_methods_exercise.document_management.document import Document
from static_and_class_methods_exercise.document_management.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def __find_by_id(entities, obj_id):
        for entity in entities:
            if entity.id == obj_id:
                return entity

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_by_id(self.categories, category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_by_id(self.topics, topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_by_id(self.documents, document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__find_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        category = self.__find_by_id(self.topics, topic_id)
        self.topics.remove(category)

    def delete_document(self, document_id):
        document = self.__find_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__find_by_id(self.documents, document_id)
        return document

    def __repr__(self):
        output = '\n'.join(str(document) for document in self.documents)
        return output


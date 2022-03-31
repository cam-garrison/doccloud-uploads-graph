"""
This Addon is used to generate a graph/chart of
upload frequency from a given user.
"""

from documentcloud.addon import AddOn


class UploadGraph(AddOn):

    def main(self):
        # fetch your add-on specific data
        username = self.data.get("name", "world")

        query = "+user:" + username

        documents = self.client.documents.search(query)

        document_dates = []

        for document in documents:
            document_dates.append(document.created_at)

        

        with open("hello.txt", "w+") as file_:
            file_.write("Hello world!")
            self.upload_file(file_)

        self.set_message("Hello World end!")
        self.send_mail("Hello World!", "We finished!")


if __name__ == "__main__":
    UploadGraph().main()

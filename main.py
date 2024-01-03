"""
This Addon is used to generate a graph/chart of
upload frequency from a given user.
"""

from documentcloud.addon import AddOn
import pandas as pd
import matplotlib


class UploadGraph(AddOn):
    def create_df(self, doc_dates):
        df = pd.DataFrame(doc_dates, columns=["datetime"])
        df["datetime"] = df["datetime"].astype("datetime64")
        df["date"] = df["datetime"].dt.date
        df = df.sort_values(by="date")
        df.insert(0, "count", range(1, 1 + len(df)))
        return df

    def main(self):
        # fetch your add-on specific data
        user_id = self.data.get("user_id")

        query = "+user:" + user_id

        documents = self.client.documents.search(query)

        document_dates = []

        for document in documents:
            document_dates.append(str(document.created_at))

        df = self.create_df(doc_dates=document_dates)
        lines = df.plot(
            y="count",
            kind="line",
            x="date",
            title=user_id + ": Uploads Over Time",
            figsize=(12, 8),
        )

        fig = lines.get_figure()
        fig.savefig("useruploads.png")

        with open("useruploads.png", "rb") as file_:
            self.upload_file(file_)

        self.set_message("Uploads Graph end!")


if __name__ == "__main__":
    UploadGraph().main()

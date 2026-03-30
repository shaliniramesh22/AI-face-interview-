import csv

class rnn:
    result_emotion={}

    def classification(self,in_data):
        features = []
        labels = []
        training_length = 0
        label='-*-'
        file = "dataset.csv"
        with open(file) as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                training_length=training_length+1
                index = row['keyword']
                emotion = row['emotion']
                labels.append(index)
                features.append(emotion)
                extract = index in in_data
                if extract:
                    label='-'+emotion
                    break
            file2 = open('emotion.txt', 'w')
            file2.writelines(str(label))
            file2.close()

    def find_emotion(self,input):

        try:
            tmp_data = self.result_emotion[input]
            ex=int(tmp_data)
            ex=ex+1
            self.result_emotion[input] = ex
        except KeyError:
            self.result_emotion[input]=1
        # print(self.result_emotion)
    def get_final_emotion(self):

        # sorted(self.result_emotion.items(), key=lambda x: x[1])

        return {k: v for k, v in sorted(self.result_emotion.items(), key=lambda item: item[1], reverse=True)}
# master_emotion=rnn()
# master_emotion.find_emotion('happy')
# master_emotion.find_emotion('happy')
# master_emotion.find_emotion('sad')
# master_emotion.find_emotion('sad')
# master_emotion.find_emotion('sad')
# master_emotion.find_emotion('sad')

#
#
# master_emotion.find_emotion('alone')
#
# print(master_emotion.get_final_emotion())

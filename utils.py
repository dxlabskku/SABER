import dataframe as df
from sklearn.utils import resample

def create_resample(train_sequence, train_enc, train_enc_senti):
    df = pd.DataFrame(list(zip(train_sequence,train_enc,train_enc_senti)), columns =['text','stance','sent'],index=None)
    blv = (df[df['stance'] == 0])
    deny = (df[df['stance'] == 1]))
    upsampled1 = resample(deny,replace=True, # sample with replacement
                          n_samples=len(blv), # match number in majority class
                          random_state=27)

    upsampled = pd.concat([blv, upsampled1])
    upsampled = upsampled.sample(frac=1)
    print("After oversample train data : ",len(upsampled))
    print("After oversampling, instances of tweet act classes in oversampled data :: ",upsampled.pol.value_counts())

    train_data = upsampled
    train_sequence = []
    train_sequence_topic = []
    train_enc = []
    train_enc_senti = []
   
    for i in range(len(train_data)):
        train_sequence.append(train_data.text.values[i])
        train_enc.append(train_data.stance.values[i])
        train_enc_senti.append(train_data.sent.values[i])

    return train_sequence, train_enc, train_enc_senti

def normalize(df):
    norm_col_list = ['len_text', 'num_hashtag', 'num_emoji', 'num_mention', 'engage']
    for col in norm_col_list: #df.columns:
        if not isinstance(df[col].values[0], str):
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df


from fastapi import FastAPI

app = FastAPI()


# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}


# Implement a /predict endpoint
@app.get("/predict")
def predict(acousticness
            ,danceability
            ,duration_ms
            ,energy
            ,explicit
            ,id
            ,instrumentalness
            ,key
            ,liveness
            ,loudness
            ,mode
            ,name
            ,release_date
            ,speechiness
            ,tempo
            ,valence
            ,artist):

    X_pred = pd.DataFrame({
            'acousticness': float(acousticness)
            ,'danceability': float(danceability)
            ,'duration_ms':int(duration_ms)
            ,'energy':float(energy)
            ,'explicit':int(explicit)
            ,'id': str(id)
            ,'instrumentalness':float(instrumentalness)
            ,'key':int(key)
            ,'liveness':float(liveness)
            ,'loudness':float(loudness)
            ,'mode':int(mode)
            ,'name':str(name)
            ,'release_date':str(release_date)
            ,'speechiness':float(speechiness)
            ,'tempo':float(tempo)
            ,'valence':float(valence)
            ,'artist':str(artist)
                            })

    pipeline = joblib.load('model.joblib')

    prediction = pipeline.predict(X_pred)
    return {

              "artist": artist,
              "name": name,
              "popularity": prediction[0]
            }

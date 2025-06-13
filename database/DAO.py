from database.DB_connect import DBConnect
from model.arco import Arco
from model.artist import Artist
from model.exhibition import Exhibition
from model.object import Object

class DAO():

   @staticmethod
   def getAllObjects():
       conn = DBConnect.get_connection()

       result = []

       cursor = conn.cursor(dictionary=True)
       query = "SELECT * FROM objects"
       cursor.execute(query)

       for row in cursor:
           result.append(Object(**row))
       cursor.close()
       conn.close()
       return result

   @staticmethod
   def getAllArtists():
       conn = DBConnect.get_connection()

       result = []

       cursor = conn.cursor(dictionary=True)
       query = "SELECT * FROM artists"
       cursor.execute(query)

       for row in cursor:
           result.append(Artist(**row))
       cursor.close()
       conn.close()
       return result

   @staticmethod
   def getAllExhibitions():
       conn = DBConnect.get_connection()

       result = []

       cursor = conn.cursor(dictionary=True)
       query = "SELECT * FROM exhibitions"
       cursor.execute(query)

       for row in cursor:
           result.append(Exhibition(**row))
       cursor.close()
       conn.close()
       return result

   @staticmethod
   def getPeso(u, v):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT eo.object_id, eo2.object_id, count(*) as peso
                    FROM exhibition_objects eo, exhibition_objects eo2
                    WHERE eo.exhibition_id = eo2.exhibition_id
                    and eo.object_id < eo2.object_id
                    and eo.object_id = %s and eo2.object_id = %s
                    GROUP BY eo.object_id, eo2.object_id"""

        cursor.execute(query, (u.object_id,v.object_id))

        for row in cursor:
           result.append(row["peso"])

        cursor.close()
        conn.close()

        if len(result) == 0:
            return None

        return result

   @staticmethod
   def getAllArchi(idMap):
       conn = DBConnect.get_connection()
       cursor = conn.cursor(dictionary=True)
       result = []
       query = """SELECT eo.object_id as o1, eo2.object_id as o2, count(*) as peso
                       FROM exhibition_objects eo, exhibition_objects eo2
                       WHERE eo.exhibition_id = eo2.exhibition_id
                       and eo.object_id < eo2.object_id
                       GROUP BY eo.object_id, eo2.object_id
                       order by peso desc"""

       cursor.execute(query)

       for row in cursor:
           result.append(Arco(idMap[row["o1"]],idMap[row["o2"]],row["peso"]))

       cursor.close()
       conn.close()

       if len(result) == 0:
           return None

       return result

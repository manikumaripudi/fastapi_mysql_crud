from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from database import connect_to_database
import uvicorn
app=FastAPI()
class Item(BaseModel):
    name:str
    address:str
    age:int
    salary:int
conn=connect_to_database()

#Route to create an item
@app.post("/items/",response_model=Item)
def create_item(item:Item):
    cursor=conn.cursor()
    query="INSERT INTO empdet2(name,address,age,salary) VALUES (%s,%s,%s,%s)"
    cursor.execute(query,(item.name,item.address,item.age,item.salary))
    conn.commit()
    cursor.close()
    return item
#Route to read the data
@app.get("/items/{item_name}",response_model=list[Item])
def read_item(item_name:str):
    cursor=conn.cursor()
    query="SELECT name,address,age,salary FROM empdet2 WHERE name=%s"
    cursor.execute(query,(item_name,))
    rows=cursor.fetchall()
    cursor.close()
    items=[]
    for row in rows:
        items.append({
            "name":row[0],
            "address":row[1],
            "age":row[2],
            "salary":row[3]
        })
    return items   
#Route to update items 
@app.put("/items/{item_id}/",response_model=Item)
def update_item(item_id:int,item:Item):
    cursor=conn.cursor()
    query="UPDATE empdet2 SET name=%s ,address=%s,age=%s,salary=%s WHERE id=%s"
    cursor.execute(query,(item.name,item.address,item.age,item.salary,item_id))
    conn.commit()
    cursor.close()
    return item    
#route to delete item
@app.delete("/del/{name}/")
def delete_item(name:str):
    cursor=conn.cursor()
    query="DELETE FROM empdet2 WHERE name=%s"
    cursor.execute(query,(name,))
    conn.commit()
    cursor.close()
    return {"Message":f"Item with '{name}' Deleted successfully"}

#route to add extra column
@app.post('/addcol')
def add_col():
  cursor=conn.cursor()
  query="ALTER TABLE empdet2 ADD email VARCHAR(255)"
  cursor.execute(query,)
  return {"Message":"Column added"}

#route to update the email
class Item1(BaseModel):
    email:str


@app.put('/email/{id}')
def add_email(id: int, data: Item1):
  cursor = conn.cursor()
  query = "UPDATE empdet2 SET email=%s WHERE id=%s"
  cursor.execute(query, (data.email, id))
  conn.commit()
  cursor.close()
  return {"result": f"Added email '{data.email}' to item with ID '{id}' successfully"}



if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=6000)

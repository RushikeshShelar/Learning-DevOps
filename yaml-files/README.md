# YAML
YAML was Perviously known as **Yet Another Markup Language** but now it stands for **YAML Aint Markup Language**. It is a Data format which is used to exchange data, it is similar to `json` and `xml` files. It is Simple Human readable langauge to store data for example configurations. `HTML` Stores Docment hence it's markup language, While `YAML` can store Object Data as Well and it is intended for data rather than documents.

In YAML you can only store data and Not add any Commands. 
YAML is Case Sensitive

Yaml is used in
- Configuration File :- Docker, Kubernetes (k8s)
- Logs, Caches, etc.

### Data Serialization and Deserialization
Process of converting the data objects into a complex data structure into a stream of bytes (Storage) is Serialization.
While the complete reverse process is knows as deserialization. 

```
                                                    |----> Memory
                                                    |
                                                    |
   Object --------> Serialiser -----> Stram of Byte ------> YAML Files
(Code + Data)                                       |
                                                    |
                                                    |----> Database
```
Data Serialization Language -> JSON, YAML, XML

## Benefits
- Simple and Easy to read
- It has Strict Syntax - Indentation is a important
- Easily convertible - JSON, XML
- Most Language use YAML
- More Powerful When Representing Complex Data 
- Various Tools available like Parsers, etc.




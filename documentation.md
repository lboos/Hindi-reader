# Hindi Reader

You can read a story in Hindi using the Hindi reader form interface at http://localhost:5000/.


## Viewing a Story

There are three stories to choose from, labeled A, B, and C. Enter one of these letters in the box and click "Submit" to view that story's title and text. For example:

```
[ 
  {
'id': 'A',
'title': 'First Day of School',
'text': 'स्कूल पहला दन...'
}, {
'id': 'B',
'title': 'My Friends',
'text': 'मेरे दोस्त...'
}, {
'id': 'C',
'title': 'The Mango Tree',
'text': 'आम का पेड़...'
  }
]
```

The stories can also be viewed using a POST request. The endpoint is http://localhost:5000/display and the story id mustbe included as {"document":\<letter\>}.


For example:

```
curl -X POST "http://localhost:5000/display" -H "Content-Type: application/json" -d '{"document":"A"}'
```

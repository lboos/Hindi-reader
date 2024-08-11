# Hindi Reader

You can read a story in Hindi using the Hindi reader form interface at http://localhost:5000/.


## Viewing a Story

There are three stories to choose from, labeled A, B, and C. Enter one of these letters in the box and click "Submit" to view that story's title and text.

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
Choosing story 'B' returns
```
**My Friends**
"मेरे दोस्त\n\nAuthor: Rukmini Banerji\n\nIllustrator: Rajeev Verma 'Banjara'\n\n\n\nमेरे बहुत सारे दोस्त हैं।\n\nमेरे कु छ दोस्त बड़े-बड़े हैं। और...\n\nकुछ दोस्त छोटे हैं।\n\nमेरे कई दोस्त बूढ़े भी हैं।\n\nऔर... कुछ नन्हे-मुन्ने भी हैं।\n\nमेरे कु छ दोस्त ऐसे भी हैं जिनकी...पूँछ भी है।\n\nऔर कुछ ऐसे जिनके... पैर ही नहीं हैं।\n\nमेरे कुछ दोस्त उड़ते हैं। और कुछ दोस्त तैरते भी हैं।\n\nओह! हो! किताबों भी तो मेरी दोस्त हैं।\n\nलेकिन, मेरा सबसे अच्छा दोस्त कौन है?\n\nकौन? कौन? कौन?\n\n\n\nमेरी माँ!\n\n\n\nAttribution Text: मेरे दोस्त (Hindi), written by Rukmini Banerji,\n\n illustrated by Rajeev Verma 'Banjara', published by Pratham Books (© Pratham Books, 2006) \n\n under a CC BY 4.0 license on StoryWeaver. Read, create and translate stories for free on www.storyweaver.org.in"
```

The stories can also be viewed using a POST request. The endpoint is http://localhost:5000/display and the story id mustbe included as {"document":\<letter\>}. For example:

```
curl -X POST "http://localhost:5000/display" -H "Content-Type: application/json" -d '{"document":"B"}'
```
returns 

```
{"id":"B","text":"\u092e\u0947\u0930\u0947 \u0926\u094b\u0938\u094d\u0924\n\nAuthor: Rukmini Banerji\n\nIllustrator: Rajeev Verma 'Banjara'\n\n\n\n\u092e\u0947\u0930\u0947 \u092c\u0939\u0941\u0924 \u0938\u093e\u0930\u0947 \u0926\u094b\u0938\u094d\u0924 \u0939\u0948\u0902\u0964\n\n\u092e\u0947\u0930\u0947 \u0915\u0941 \u091b \u0926\u094b\u0938\u094d\u0924 \u092c\u0921\u093c\u0947-\u092c\u0921\u093c\u0947 \u0939\u0948\u0902\u0964 \u0914\u0930...\n\n\u0915\u0941\u091b \u0926\u094b\u0938\u094d\u0924 \u091b\u094b\u091f\u0947 \u0939\u0948\u0902\u0964\n\n\u092e\u0947\u0930\u0947 \u0915\u0908 \u0926\u094b\u0938\u094d\u0924 \u092c\u0942\u0922\u093c\u0947 \u092d\u0940 \u0939\u0948\u0902\u0964\n\n\u0914\u0930... \u0915\u0941\u091b \u0928\u0928\u094d\u0939\u0947-\u092e\u0941\u0928\u094d\u0928\u0947 \u092d\u0940 \u0939\u0948\u0902\u0964\n\n\u092e\u0947\u0930\u0947 \u0915\u0941 \u091b \u0926\u094b\u0938\u094d\u0924 \u0910\u0938\u0947 \u092d\u0940 \u0939\u0948\u0902 \u091c\u093f\u0928\u0915\u0940...\u092a\u0942\u0901\u091b \u092d\u0940 \u0939\u0948\u0964\n\n\u0914\u0930 \u0915\u0941\u091b \u0910\u0938\u0947 \u091c\u093f\u0928\u0915\u0947... \u092a\u0948\u0930 \u0939\u0940 \u0928\u0939\u0940\u0902 \u0939\u0948\u0902\u0964\n\n\u092e\u0947\u0930\u0947 \u0915\u0941\u091b \u0926\u094b\u0938\u094d\u0924 \u0909\u0921\u093c\u0924\u0947 \u0939\u0948\u0902\u0964 \u0914\u0930 \u0915\u0941\u091b \u0926\u094b\u0938\u094d\u0924 \u0924\u0948\u0930\u0924\u0947 \u092d\u0940 \u0939\u0948\u0902\u0964\n\n\u0913\u0939! \u0939\u094b! \u0915\u093f\u0924\u093e\u092c\u094b\u0902 \u092d\u0940 \u0924\u094b \u092e\u0947\u0930\u0940 \u0926\u094b\u0938\u094d\u0924 \u0939\u0948\u0902\u0964\n\n\u0932\u0947\u0915\u093f\u0928, \u092e\u0947\u0930\u093e \u0938\u092c\u0938\u0947 \u0905\u091a\u094d\u091b\u093e \u0926\u094b\u0938\u094d\u0924 \u0915\u094c\u0928 \u0939\u0948?\n\n\u0915\u094c\u0928? \u0915\u094c\u0928? \u0915\u094c\u0928?\n\n\n\n\u092e\u0947\u0930\u0940 \u092e\u093e\u0901!\n\n\n\nAttribution Text: \u092e\u0947\u0930\u0947 \u0926\u094b\u0938\u094d\u0924 (Hindi), written by Rukmini Banerji,\n\n illustrated by Rajeev Verma 'Banjara', published by Pratham Books (\u00a9 Pratham Books, 2006) \n\n under a CC BY 4.0 license on StoryWeaver. Read, create and translate stories for free on www.storyweaver.org.in","title":"My Friends"}
```
(In the terminal the Hindi is not rendered correctly.)

import 'dart:html';

import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context){
    

    return MaterialApp(
      title: 'Welcome to Flutter',
      home: RandomWords(),
    );
  }
}

// #docregion _RandomWordsState, RWS-class-only
class _RandomWordsState extends State<RandomWords> {

  final _suggestions = <WordPair>[];
  final _biggerFont = const TextStyle(fontSize: 18);
  // #enddocregion RWS-class-only
  @override
  Widget build(BuildContext context) {
    return Scaffold (                     // Add from here... 
      appBar: AppBar(
        title: Text('Startup Name Generator'),
      ),
      body: _buildSuggestions(),
    );              
  }

  Widget _buildSuggestions() {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      // The itemBuilder callback is called once per suggested 
      // word pairing, and places each suggestion into a ListTile
      // row. For even rows, the function adds a ListTile row for
      // the word pairing. For odd rows, the function adds a 
      // Divider widget to visually separate the entries. Note that
      // the divider may be difficult to see on smaller devices.
      itemBuilder: (BuildContext _context, int i) {
        // Add a one-pixel-high divider widget before each row 
        // in the ListView.
        if (i.isOdd) {
          return Divider();
        }

        // The syntax "i ~/ 2" divides i by 2 and returns an 
        // integer result.
        // For example: 1, 2, 3, 4, 5 becomes 0, 1, 1, 2, 2.
        // This calculates the actual number of word pairings 
        // in the ListView,minus the divider widgets.
        final int index = i ~/ 2;
        // If you've reached the end of the available word
        // pairings...
        if (index >= _suggestions.length) {
          // ...then generate 10 more and add them to the 
          // suggestions list.
          _suggestions.addAll(generateWordPairs().take(10));
        }
        return _buildRow(_suggestions[index]);
      }
    );
  }

  Widget _buildRow(WordPair pair) {
    return ListTile(
      title: Text(
        pair.asPascalCase,
        style: _biggerFont,
      ),
    );
  }

  // #docregion RWS-class-only
}
// #enddocregion _RandomWordsState, RWS-class-only

// #docregion RandomWords
class RandomWords extends StatefulWidget {
  @override
  State<RandomWords> createState() => _RandomWordsState();
}
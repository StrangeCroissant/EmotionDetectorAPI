import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:english_words/english_words.dart';
import 'package:provider/provider.dart';
import 'package:emotion_detector/models_page.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
//custom packages
// import 'package:emotion_detector/nav_rail.dart';
void main() async{
  await dotenv.load(fileName: '.env');
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => MyAppState(),
      child: ChangeNotifierProvider(
        create: (context) => NavigationState(),
        child: MaterialApp(
          title: 'Emotion Detection App',
          theme: ThemeData(
            useMaterial3: true,
            colorScheme: ColorScheme.fromSeed(seedColor: Color.fromARGB(1, 0, 0, 125)),
          ),
          home: MyHomePage(),
        ),
      ),
    );
  }
}

class MyAppState extends ChangeNotifier {
  var currentText = ''; // Store the current text input
  
  void updateText(String newText) {
    currentText = newText;
    notifyListeners();
  }
}

class NavigationState extends ChangeNotifier {
  int _selectedIndex = 0;

  int get selectedIndex => _selectedIndex;

  set selectedIndex(int index) {
    _selectedIndex = index;
    notifyListeners();
  }
}
class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final navigationState = Provider.of<NavigationState>(context);

    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text('Emotion Classifier on Text'),
        titleTextStyle: TextStyle(
          color: Theme.of(context).colorScheme.onPrimaryContainer,
          fontSize: 24,
          fontWeight: FontWeight.bold,
          letterSpacing: 2,
        ),
      ),
      body: Row(
        children: [
          SafeArea(
            child: NavigationRail(
              extended: true,
              destinations: [
                NavigationRailDestination(
                  icon: Icon(Icons.home),
                  label: Text('Classifier'),
                ),

                NavigationRailDestination(
                  icon: Icon(Icons.admin_panel_settings),
                  label: Text('Model Selection'),
                ),
              ],
              trailing:
                Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    FloatingActionButton(
                      child: Icon(Icons.info),
                      onPressed: () {
                        showDialog(
                          context: context,
                          builder: (BuildContext context) {
                            return AlertDialog(
                              title: Text('Information'),
                              content: Text(dotenv.env['INFO_STR']!),
                              actions: <Widget>[
                                TextButton(
                                  child: Text('Close'),
                                  onPressed: () {
                                    Navigator.of(context).pop();
                                  },
                                ),
                              ],
                            );
                          },
                        );
                      },
                    ),
                  ],
                ),
              selectedIndex: navigationState.selectedIndex,
              onDestinationSelected: (index) {
                navigationState.selectedIndex = index;
                if (index == 0) {
                  // Reset the selectedIndex to 0 to reload the main page
                  navigationState.selectedIndex = 0;
                } else if (index == 1) {
                  Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (context) => ModelSelectionPage(),
                    ),
                  );
                }
              },
            ),
          ),
          Expanded(
            child: Container(
              color: Theme.of(context).colorScheme.primaryContainer,
              child: GeneratorPage(),
            ),
          ),
        ],
      ),
    );
  }
}

class GeneratorPage extends StatefulWidget {
  @override
  _GeneratorPageState createState() => _GeneratorPageState();
  }

class _GeneratorPageState extends State<GeneratorPage> {
  String _classificationResult = '';

  @override
  Widget build(BuildContext context) {
    var appState = context.watch<MyAppState>();

    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          if (_classificationResult.isNotEmpty)
            Container(
              color: Theme.of(context).colorScheme.secondaryContainer,
              padding: EdgeInsets.all(15.0),
              child: Text(
                
                'Classification Result: $_classificationResult',
                style: TextStyle(
                  fontSize: 24.0,
                  fontWeight: FontWeight.bold, 
                  color: Theme.of(context).colorScheme.primary,
                  ),
              ),
            ),
          TextField(
            onChanged: (text) {
              appState.updateText(text); // Update the text input
            },
            decoration: InputDecoration(
              hintText: 'Enter your text here',
              contentPadding: EdgeInsets.all(20.0),
              constraints: BoxConstraints(maxWidth: 500),
              fillColor: Theme.of(context).colorScheme.secondaryContainer,
              border: OutlineInputBorder(),
              counterText: '0 characters',
            ),
          ),
          SizedBox(height: 15),
          ElevatedButton(
            onPressed: () {
              sendText(appState.currentText).then((result) {
                setState(() {
                  _classificationResult = result;
                });
              });
            },
            child: Text('Classify'),
          ),
        ],
      ),
    );
  }
}
class BigCard extends StatelessWidget {
  const BigCard({
    super.key,
    required this.pair,
  });

  final WordPair pair;

  @override
  Widget build(BuildContext context) {
    var theme = Theme.of(context);
    var style = theme.textTheme.displaySmall!.copyWith(
      color: theme.colorScheme.primary,
    );

    return Card(
      color: theme.colorScheme.secondaryContainer,
      child: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Text(
          pair.asPascalCase, // Displaying the current word pair
          style: style,
        ),
      ),
    );
  }
}

Future<String> sendText(String text) async {
  var url = Uri.parse(dotenv.env['INFERENCE_OPENAI']!);
  var response = await http.post(
    url,
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'text': text}),
  );

  if (response.statusCode == 200) {
    // Handle successful response
    var jsonResponse = jsonDecode(response.body);
    var classificationResult = jsonResponse['response'];
    print('Classification Result: $classificationResult');
    return classificationResult;
  } else {
    // Handle error
    print('Error: ${response.reasonPhrase}');
    return '';
  }
}
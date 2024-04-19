import 'package:flutter/material.dart';

class ModelSelectionPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Model Selection'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              decoration: BoxDecoration(
                color: Theme.of(context).colorScheme.primaryContainer,
                borderRadius: BorderRadius.circular(8),

              ),
              padding: EdgeInsets.all(16),
              constraints: BoxConstraints(
                maxWidth: 300,
              ),
              child: Text(
                'Select a model to generate text. Please note that OpenAI requires an API key witch access to the gpt3.5-turbo model.',
                style: TextStyle(
                  fontSize: 16,
                  color: Theme.of(context).colorScheme.onPrimaryContainer,
                ),
              ),
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                // Handle the selection of OpenAI model
                // For example, you can navigate to a new page or perform any action
                // You can replace this with your own logic
                print('OpenAI model selected');
              },
              child: Text('OpenAI'),
            ),
            SizedBox(height: 16), // Add space of 16 pixels between the buttons
            ElevatedButton(
              onPressed: () {
                // Handle the selection of Mistral model
                // For example, you can navigate to a new page or perform any action
                // You can replace this with your own logic
                print('Mistral model selected');
              },
              child: Text('Mistral'),
            ),
            SizedBox(height: 16), // Add space of 16 pixels between the buttons
            ElevatedButton(
              onPressed: () {
                // Handle the selection of BERT model
                // For example, you can navigate to a new page or perform any action
                // You can replace this with your own logic
                print('BERT model selected');
              },
              child: Text('BERT'),
            ),
            
          ],
        ),
      ),
    );
  }
}

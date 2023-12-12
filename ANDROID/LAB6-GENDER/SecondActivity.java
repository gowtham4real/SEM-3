package com.example.gender;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

public class SecondActivity extends AppCompatActivity {
    TextView greetingTextView;
    ImageView pictureImageView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        greetingTextView = findViewById(R.id.name);
        pictureImageView = findViewById(R.id.image);

        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            String name = extras.getString("Name");
            String gender = extras.getString("gen");

            String greeting = "Hello, " + name + "!";
            greetingTextView.setText(greeting);

            if (gender.equals("Male")) {
                pictureImageView.setImageResource(R.drawable.m);
            } else if (gender.equals("Female")) {
                pictureImageView.setImageResource(R.drawable.f);
            }
        }
    }
}

package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class SecondActivity extends AppCompatActivity
{
    TextView t;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_seccond);
        String a= getIntent().getStringExtra("username");
        t=findViewById(R.id.txt);
        t.setText("Welcome "+a);
    }
}

package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity
{
    EditText user,mail,contact;
    Button b;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        user=findViewById(R.id.name);
        mail=findViewById(R.id.email);
        contact=findViewById(R.id.phone);
        b=findViewById(R.id.btn);
    }
    public void verify(View view)
    {
        String name=user.getText().toString();
        String gmail=mail.getText().toString();
        if (gmail.endsWith("@gmail.com"))
        {
            Intent i=new Intent(this,SecondActivity.class);
            i.putExtra("username",name);
            startActivity(i);
        }
        else
        {
            Toast.makeText(this, "Invalid Login",Toast.LENGTH_LONG).show();
        }

    }
}

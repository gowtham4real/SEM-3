package com.example.gender;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

public class MainActivity extends AppCompatActivity
{
    EditText e1;
    Spinner s1;
    Button b1;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        e1=(EditText) findViewById(R.id.name);
        s1=(Spinner) findViewById(R.id.spin);
        b1=(Button) findViewById(R.id.btn);

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(
                this,
                R.array.Gender,
                android.R.layout.simple_spinner_item
        );

        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        s1.setAdapter(adapter);



    }


    public void gendercheck(View view)
    {
        String a=s1.getSelectedItem().toString().trim();
        String w=e1.getText().toString();
        Intent intent=new Intent(this,SecondActivity.class);
        intent.putExtra("Name", w);
        intent.putExtra("gen",a);
        startActivity(intent);

    }
}

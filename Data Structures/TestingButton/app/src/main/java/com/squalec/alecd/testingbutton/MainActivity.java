package com.squalec.alecd.testingbutton;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity{


    private ArrayList<Button> buttonArrayList = new ArrayList<Button>();
    private ArrayList<LinearLayout> linearLayoutArrayList = new ArrayList<LinearLayout>();
    private ArrayList<Integer> countTextViews = new ArrayList<Integer>();

    private LinearLayout root;
    private LinearLayout linearLayout1;
    private Button btnAddTextToLayout;
    private TextView textView;
    LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);


    private int count =0;
    private int count2 = 0;

    private final int linearLayoutBaseID = 10000;
    private final int addTextToLayoutBaseID = 20000;


    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        root = (LinearLayout)this.findViewById(R.id.root_layout);



        LinearLayout linearLayout2 = new LinearLayout(this);
        linearLayout2.setOrientation(LinearLayout.VERTICAL);


        Button addLinearLayout = new Button(this);
        addLinearLayout.setText("Add New Layout");
        addLinearLayout.setId(100);

        addLinearLayout.setOnClickListener(new addLinearLayoutClick());


        //Add Buttons and views
        linearLayout2.addView(addLinearLayout);

        // add generated layouts to root layout view
        root.addView(linearLayout2);
    }

    private void addLinearLayoutClicked(View view){
        count++;
        countTextViews.add(0);



        linearLayout1 = new LinearLayout(MainActivity.this);
        linearLayout1.setLayoutParams(layoutParams);
        linearLayout1.setOrientation(LinearLayout.VERTICAL);
        linearLayout1.setId(count + linearLayoutBaseID);
        linearLayout1.setBackgroundColor(Color.BLUE);
        linearLayout1.setElevation(200);
        linearLayoutArrayList.add(linearLayout1);

        btnAddTextToLayout = new Button(this);
        btnAddTextToLayout.setId(addTextToLayoutBaseID + count);
        btnAddTextToLayout.setText(Integer.toString(addTextToLayoutBaseID+count));
        buttonArrayList.add(btnAddTextToLayout);

        for(int i = 0; i < buttonArrayList.size(); i++) {
            Button tempButton = buttonArrayList.get(i);
            tempButton.setOnClickListener(new btnAddTextToLayoutClick());
        }

        linearLayout1.addView(btnAddTextToLayout);
        root.addView(linearLayout1);
    }

    private void btnAddTextToLayoutClicked(View view){
        count2++;
        int id = view.getId() -addTextToLayoutBaseID;
        int textViewCount = (countTextViews.get(id-1)+1);

        countTextViews.set(id-1, textViewCount);

        textView = new TextView(this);
        textView.setText(Integer.toString(countTextViews.get(id-1)));

        for(int i = 0; i<linearLayoutArrayList.size(); i++){
            LinearLayout tempLinearLayout = linearLayoutArrayList.get(i);
            if(tempLinearLayout.getId() - linearLayoutBaseID == id){
                tempLinearLayout.addView(textView);
            }
        }
    }

    class addLinearLayoutClick implements View.OnClickListener{
        @Override
        public void onClick(View view){
            addLinearLayoutClicked(view);
        }
    }

    class btnAddTextToLayoutClick implements View.OnClickListener{
        @Override
        public void onClick(View view){
            btnAddTextToLayoutClicked(view);
        }
    }
}

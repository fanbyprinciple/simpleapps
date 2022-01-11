package com.example.splash_page_stopwatch;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.graphics.Typeface;
import android.media.AudioManager;
import android.media.ToneGenerator;
import android.os.Bundle;
import android.os.SystemClock;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.Chronometer;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.Console;

public class StopWatchAct extends AppCompatActivity {

    Button btnstart, btnstop;
    ImageView icanchor;
    Animation roundingalone;
    Chronometer timerHere;
    EditText timerBeepFreq;
    int limit=30;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_stop_watch);

        btnstart = findViewById(R.id.btnstart);
        btnstop = findViewById(R.id.btnstop);
        icanchor = findViewById(R.id.icanchor);
        timerHere = findViewById(R.id.timerHere);
        timerBeepFreq = findViewById(R.id.timerBeepFreq);
        timerBeepFreq.setText("10");
        timerBeepFreq.setGravity(Gravity.CENTER_HORIZONTAL);

        btnstop.setAlpha(0);

        roundingalone = AnimationUtils.loadAnimation(this, R.anim.roundingalone);

        Typeface MLight = Typeface.createFromAsset(getAssets(), "fonts/MLight.ttf");
        Typeface MMedium = Typeface.createFromAsset(getAssets(), "fonts/MMedium.ttf");
        Typeface MRegular = Typeface.createFromAsset(getAssets(), "fonts/MRegular.ttf");

        btnstart.setTypeface(MMedium);


        btnstart.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                icanchor.startAnimation(roundingalone);
                btnstop.animate().alpha(1).translationY(-100).setDuration(300).start();
                btnstart.animate().alpha(0).setDuration(300).start();

                timerHere.setBase(SystemClock.elapsedRealtime());
                timerHere.start();
//                if (String.valueOf(timerBeepFreq.getText()) != ""){
//                    Toast toast=Toast.makeText(getApplicationContext(),limit,Toast.LENGTH_SHORT);
//                    toast.setMargin(50,50);
//                    toast.show();
//
//                } else {
//                    limit = Integer.valueOf(String.valueOf(timerBeepFreq.getText()));
//                }
                limit = Integer.valueOf(String.valueOf(timerBeepFreq.getText()));

                ToneGenerator toneGen1 = new ToneGenerator(AudioManager.STREAM_MUSIC, 100);
                toneGen1.startTone(ToneGenerator.TONE_CDMA_PIP,150);

            }
        });



        timerHere.setOnChronometerTickListener(new Chronometer.OnChronometerTickListener() {
                                                   @Override
                                                   public void onChronometerTick(Chronometer chronometer) {
                                                       long initial, elapsed;
//                                                       long counter = 0;
                                                       initial = SystemClock.elapsedRealtime() - chronometer.getBase();
                                                       elapsed = initial;
//                                                       Log.d("executed", String.valueOf(elapsed%(limit * 1000)));
                                                       if (elapsed % (limit * 1000) <= 1000) {
                                                           ToneGenerator toneGen1 = new ToneGenerator(AudioManager.STREAM_MUSIC, 100);
                                                           toneGen1.startTone(ToneGenerator.TONE_CDMA_ABBR_ALERT, 300);

//                                                           counter = counter + 1;
                                                           if (chronometer.getCurrentTextColor() == Color.WHITE){
                                                               chronometer.setTextColor(Color.RED);
                                                           } else {
                                                               chronometer.setTextColor(Color.WHITE);
                                                           }
//                                                           Log.d("executed", String.valueOf(counter));
//                        Toast toast=Toast.makeText(getApplicationContext(), (int) elapsed,Toast.LENGTH_SHORT);
//                        toast.setMargin(50,50);
//                        toast.show();

                                                       }
                                                   }
                                               });

        btnstop.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                  icanchor.clearAnimation();
                  timerHere.stop(); //pause
                  btnstop.animate().alpha(0).translationY(100).setDuration(300).start();
                  btnstart.animate().alpha(1).setDuration(300).start();

//                  ToneGenerator toneGen1 = new ToneGenerator(AudioManager.STREAM_MUSIC, 100);
//                  toneGen1.startTone(ToneGenerator.TONE_CDMA_PIP,150);
            }
        });



    }
}
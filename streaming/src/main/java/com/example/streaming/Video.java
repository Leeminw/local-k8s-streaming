package com.example.streaming;

import lombok.*;
import org.hibernate.annotations.GeneratorType;
import org.springframework.data.mongodb.core.mapping.Document;

import javax.persistence.*;

@Getter
@Setter
@Document(collection = "video_list")
public class Video {

    public String id;
    private String title;
    private String url;
    private String on;

    private String description;

    public Video(){

    }


    public Video(String id, String title, String url, String on, String description) {
        this.id = id;
        this.title = title;
        this.url = url;
        this.on = on;
        this.description = description;
    }
    @Override
    public String toString() {
        return String.format(
            "{ title='%s', url='%s' , on='%s', description = '%s' }",
            title,url,on,description);
      }
}

package com.example.streaming;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class VideoService {

    @Autowired
    private VideoRepository videoRepository;

    public String selectVideo(String title) {
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            if (videoRepository.findByTitle(title) == null) {

                return String.format("user title : %s not exist!!", title);
            } else {
                return objectMapper.writeValueAsString(videoRepository.findByTitle(title));
            }
        } catch (JsonProcessingException e) {
            e.printStackTrace();
            return "ERROR";
        }
    }

    public List<Video> findAllVideos(){
       return videoRepository.findAll();
    }

}
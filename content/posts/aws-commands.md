---
date: 2020-06-16 12:00
title: AWS commands
category: English
tags: cloud, cloud computing, saas, iaas, paas, aws, amazon, development, CLI, iam, transcribe, text-to-speech, brew
---

All commandes below relies on the latest version of [aws-cli](https://github.com/aws/aws-cli).

macOS install:

    :::shell-session
    $ brew install awscli
    (...)
    $ aws --version
    aws-cli/2.0.19 Python/3.8.3 Darwin/19.5.0 botocore/2.0.0dev23


## Authentication

  * Register default profile:

        :::shell-session
        $ aws configure
 
  * Register additional profile:

        :::shell-session
        $ aws configure --profile bob

  * List access keys:
  
        :::shell-session
        $ aws iam list-access-keys

  * List access keys of another profile:
  
        :::shell-session
        $ aws iam --profile bob list-access-keys


## Amazon Transcribe

  * Fetch all names of the first 100 [transcription jobs](https://docs.aws.amazon.com/cli/latest/reference/transcribe/list-transcription-jobs.html):

        :::shell-session
        $ aws transcribe list-transcription-jobs --query '[TranscriptionJobSummaries[*].TranscriptionJobName]' --max-results 100 --output text
        
  * [Get URL of the transcript](https://docs.aws.amazon.com/cli/latest/reference/transcribe/get-transcription-job.html) produced by `my_job_name` job:

        :::shell-session
        $ aws transcribe get-transcription-job --transcription-job-name my_job_name --query '[TranscriptionJob.Transcript.TranscriptFileUri]' --output text
        
  * Same as above but save the transcript content directly to a local `transcript.txt` file:

        :::shell-session
        $ AWS_PAGER="" aws transcribe get-transcription-job --transcription-job-name my_job_name --query '[TranscriptionJob.Transcript.TranscriptFileUri]' --output text | wget -i - -O - | jq --raw-output '.results.transcripts[0].transcript' > transcript.txt        
        
  * Putting it all together, here is how do download all transcripts from all your jobs:

        :::shell
        for JOB_ID in $(aws transcribe list-transcription-jobs --query '[TranscriptionJobSummaries[*].TranscriptionJobName]' --max-results 100 --output text);
            do AWS_PAGER="" aws transcribe get-transcription-job --transcription-job-name "$JOB_ID" --query '[TranscriptionJob.Transcript.TranscriptFileUri]' --output text | wget -i - -O - | jq --raw-output '.results.transcripts[0].transcript' > "$JOB_ID".txt;
        done

# Paraphrase and Corrupted-Control Test for Synthetic Instruction Priming

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `paraphrase-and-corrupted-control-test-for-synthetic-instru-92fdef2d6c`
Run ID: `paraphrase-and-corrupted-control-test-for-synthetic-instru-92fdef2d6c-20260526T164221297749+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Synthetic Instruction Priming in Pretraining: enoch://control-plane/projects/synthetic-instruction-priming-in-pretraining-f18a14aa93b7/runs/synthetic-instruction-priming-in-pretraining-f18a14aa93b7-20260526T092541099118+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/026a37900b96

## What looked useful

Paraphrase accuracy alone is not sufficient evidence for semantic synthetic instruction priming: in this balanced controlled test, far paraphrase accuracy was about 0.763-0.767, but nonce-corrupt controls were about 0.744-0.752 and corrupt-trained models transferred around 0.714-0.730 to clean/paraphrased prompts.

## Boundaries and scale limits

CPU-only toy classifier; no pretrained LLM, no real instruction benchmark, four synthetic string tasks, 20 seeds. The result is a Tier-1 mechanism/control test, not publication-grade model evidence.

## Claim scope

In a small controlled synthetic string-task classifier, clean synthetic instruction priming transfers strongly to lexically close paraphrases and modestly to synonym-heavy paraphrases, but corrupted controls are also high and fail the required +0.15 separation threshold.

## Why it stopped

Tier-1 controlled test produced a useful but no-paper mixed/negative result: the paraphrase-transfer signal did not separate from corrupted controls, so this is an early control failure rather than full validation.

## Recommended next action

Run a bounded pretrained-small-LM replication with balanced tasks and the same corrupted-training controls; stop if corrupted controls again come within 15 percentage points of clean far-paraphrase transfer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Small-LM Replication of Balanced Paraphrase and Corrupted-Control Priming
- Success threshold: Clean-trained far paraphrase accuracy >= 0.75 and at least 0.15 above both nonce-corrupt evaluation and corrupted-trained clean/paraphrase transfer; corrupted and wrong-instruction controls <= 0.60.
- Stop condition: Stop as unsupported if corrupted controls exceed 0.60 or come within 0.15 of clean far-paraphrase accuracy after balanced-data validation.

## Evidence references

- Artifact root: `<local-path>/projects/paraphrase-and-corrupted-control-test-for-synthetic-instru-92fdef2d6c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

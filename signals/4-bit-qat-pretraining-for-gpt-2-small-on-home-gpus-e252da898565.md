# 4-Bit QAT Pretraining for GPT-2-Small on Home GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-qat-pretraining-for-gpt-2-small-on-home-gpus-e252da898565`
Run ID: `4-bit-qat-pretraining-for-gpt-2-small-on-home-gpus-e252da898565-20260523T234512828121+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/84a15477df72

## What looked useful

W4 projection QAT reduced fixed held-out synthetic loss without NaN/Inf. At 13.8M parameters, baseline eval loss improved by -1.4584 and W4 QAT by -1.3909, with W4 about 7% slower. At GPT-2-small geometry, W4 QAT fit in about 1.27 GiB peak PyTorch allocation and improved eval loss by -0.0562 over 40 measured steps. W4A4 was stable but weaker, improving eval loss by -1.1573 versus -1.4584 for baseline on the 13.8M run.

## Boundaries and scale limits

Synthetic deterministic token stream only; short runs of 80 measured steps at 13.8M parameters and 40 measured steps at 123.8M parameters; embeddings and LM head not quantized; fake quantization only, not packed int4 kernels; no real-corpus perplexity or long-horizon pretraining evidence.

## Claim scope

Naive straight-through 4-bit fake-quantized GPT-2 transformer projection training is locally runnable and numerically stable on a GB10 home GPU for short synthetic-token probes, including a 123.8M-parameter GPT-2-small-geometry model.

## Why it stopped

Closed as no-paper useful signal because the evidence is short, synthetic, and fake-quantized; it supports local stability but not competitive GPT-2-small pretraining practicality.

## Recommended next action

Run a bounded real-corpus GPT-2-small follow-up comparing baseline, W4 projection QAT, and W4A4 QAT on validation perplexity over a fixed token budget before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small W4/W4A4 QAT validation-perplexity probe
- Success threshold: W4 QAT validation perplexity remains within 5% of BF16 baseline at the final bounded checkpoint with no NaN/Inf and no more than 25% throughput loss; W4A4 must be reported separately and should not be considered successful unless it also meets the same quality bound.
- Stop condition: Stop if W4 QAT validation perplexity is more than 10% worse than baseline after the first two evaluation checkpoints, if NaN/Inf appears, or if projected runtime exceeds the local budget without checkpointed evidence.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-qat-pretraining-for-gpt-2-small-on-home-gpus-e252da898565`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

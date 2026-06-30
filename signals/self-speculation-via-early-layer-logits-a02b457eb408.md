# Self-Speculation via Early-Layer Logits

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculation-via-early-layer-logits-a02b457eb408`
Run ID: `self-speculation-via-early-layer-logits-a02b457eb408-20260609T171633882093+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/39c5b43f8902

## What looked useful

Expected one-token speculative acceptance reached 0.4746 at distilgpt2 block 5/6 and 0.5388 at gpt2 block 11/12 versus unigram baselines near 0.09, while mid-layer acceptance stayed low enough to make practical speedup doubtful without additional mechanisms.

## Boundaries and scale limits

CPU-only bounded evaluation; 4096 token positions for distilgpt2 and 2048 for gpt2; no actual multi-token speculative decoder, KV-cache implementation, serving benchmark, large model, or broad corpus validation.

## Claim scope

On a fixed local text corpus with pretrained distilgpt2 and gpt2, projecting intermediate hidden states through the model final norm and LM head yields draft distributions that are much closer to final logits than a unigram baseline, but useful acceptance appears only at late layers.

## Why it stopped

Bounded mechanism probe supports late-layer draft closeness but does not support a practical self-speculation speedup claim; the result is not a full validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the concrete next test is an actual cache-reusing multi-token self-speculative decoder on gpt2/distilgpt2 that reports matched-distribution wall-clock speedup or slowdown.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Wall-clock self-speculative decoding with late-layer GPT-2 exits
- Success threshold: At least 1.10x wall-clock tokens/sec over standard decoding on both distilgpt2 and gpt2 with distribution-preserving verification and no more than 5% additional memory.
- Stop condition: Stop if the implemented decoder is slower than baseline at the best late-layer cutoff or if exact verification cannot preserve the target distribution.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculation-via-early-layer-logits-a02b457eb408`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

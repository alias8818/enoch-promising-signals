# 8-bit Adam with normalized gradients for tiny-VRAM training on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adam-with-normalized-gradients-for-tiny-vram-training-on-gb10-1685fa5f06c3`
Run ID: `8-bit-adam-with-normalized-gradients-for-tiny-vram-training-on-gb10-1685fa5f06c3-20260614T060953717375+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5687ed737c89

## What looked useful

8-bit Adam state compression is a viable tiny-VRAM mechanism in this bounded GB10 proxy, but normalized gradients did not provide a robust improvement and should not be presented as a positive result without a deeper tuned benchmark.

## Boundaries and scale limits

Evidence is limited to a synthetic Markov-token task, 200-step runs, three seeds for the main comparison, one simple blockwise quantizer, and a non-fused PyTorch prototype. It does not validate real-corpus GPT-2-small-class training, 7B-class training, long-run stability, or fused-kernel throughput.

## Claim scope

On a 10.7M-parameter synthetic Transformer next-token task on GB10, blockwise 8-bit Adam optimizer states reduced persistent optimizer-state memory by about 75% versus AdamW and trained cleanly; adding per-tensor RMS-normalized gradients was seed-sensitive and not robust across tested learning rates.

## Why it stopped

Bounded proxy evidence supports 8-bit optimizer-state memory savings but gives mixed/negative evidence for the normalized-gradient addition; this is not a full validation and not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should compare unnormalized 8-bit Adam against a safer normalized-gradient variant on a real small text corpus with a predefined LR schedule and held-out perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tuned comparison of 8-bit Adam with safer gradient normalization
- Success threshold: Normalized-gradient 8-bit Adam must keep optimizer-state bytes within 5% of unnormalized 8-bit Adam and improve mean held-out perplexity by at least 3% versus unnormalized 8-bit Adam without any seed diverging or regressing by more than 5%.
- Stop condition: Stop if the best normalized-gradient variant is worse than unnormalized 8-bit Adam on two of three seeds, diverges on any seed, or requires more than a 2x throughput penalty in the non-fused prototype.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-with-normalized-gradients-for-tiny-vram-training-on-gb10-1685fa5f06c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

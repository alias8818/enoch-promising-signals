# BPE-tokenized WikiText HMT vs parameter-matched mini-GPT confirmation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bpe-tokenized-wikitext-hmt-vs-parameter-matched-mini-gpt-c-3181a9e2e7`
Run ID: `bpe-tokenized-wikitext-hmt-vs-parameter-matched-mini-gpt-c-3181a9e2e7-20260524T103251185680+0000`

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

- Parent run decision: Hierarchical memory tokens for 4k local GPT-2 training: enoch://control-plane/projects/hierarchical-memory-tokens-for-4k-local-gpt-2-training-7da2b07de8b1/runs/hierarchical-memory-tokens-for-4k-local-gpt-2-training-7da2b07de8b1-20260524T080336170772+0000
- Parent run decision: Parameter-matched mini-GPT-2 HMT language-model validation: enoch://control-plane/projects/parameter-matched-mini-gpt-2-hmt-language-model-validation-8032a50ebc/runs/parameter-matched-mini-gpt-2-hmt-language-model-validation-8032a50ebc-20260524T102240224648+0000

## What looked useful

HMT mean best validation loss was 5.3498 versus mini-GPT 5.3956, but the no-memory segmented control was 5.3535. The HMT-vs-control gain was only 0.0037 nats/token, below the 0.02 mechanism threshold, so the memory mechanism is not confirmed.

## Boundaries and scale limits

WikiText-2 only; three fixed seeds; 800 steps; 192-token context; HMT/control have about 1.2% more parameters than baseline; no WikiText-103, long-context, or large-model validation.

## Claim scope

Small 7M-parameter GPT-2-BPE WikiText-2 training at 800 optimizer steps and 192-token context: the HMT-style segmented model improves validation loss versus a near-parameter-matched mini-GPT baseline, but recurrent memory adds only a negligible gain over the no-memory segmented control.

## Why it stopped

Direct Tier-2 small-model evidence with fixed seeds, baseline, and ablation did not support the recurrent-memory mechanism; the positive baseline gap is mostly reproduced by the no-memory control.

## Recommended next action

Stop this HMT confirmation as no-paper: preserve the useful signal that segmentation/local attention may explain the gain, and only pursue a separate bounded follow-up on segmented no-memory Transformers if desired.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Segmented local-attention mini-Transformer vs full-context mini-GPT on BPE WikiText
- Success threshold: Segmented no-memory model beats exact-parameter full-context GPT by at least 0.03 nats/token mean best validation loss across three seeds without any seed reversal larger than 0.01.
- Stop condition: Stop if exact parameter matching or longer training removes the segmented model advantage, or if gains appear only at one segment size.

## Evidence references

- Artifact root: `<local-path>/projects/bpe-tokenized-wikitext-hmt-vs-parameter-matched-mini-gpt-c-3181a9e2e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Self-speculative decoding via early-exit draft head on same model

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `self-speculative-decoding-via-early-exit-draft-head-on-same-model-52b539aeb3d4`
Run ID: `self-speculative-decoding-via-early-exit-draft-head-on-same-model-52b539aeb3d4-20260620T203312348227+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fffce6da15c8

## What looked useful

A same-model early-exit draft head needs direct auxiliary supervision; when supervised, it can become a high-acceptance draft source without hurting final accuracy on a simple learnable task. The control without early loss learned the final task but produced unusable early drafts.

## Boundaries and scale limits

Synthetic toy distribution only; no natural-language corpus, no Llama/GPT-2-scale model, no sampling-quality evaluation, no optimized KV-cache reuse, and only a naive PyTorch wall-clock benchmark.

## Claim scope

On a tiny 4-layer decoder-only transformer trained on a simple synthetic next-token language, an auxiliary layer-2 early-exit LM head preserved final-head accuracy while raising early/final argmax agreement from 0.0116 to 0.9892 and enabling full acceptance for gamma 2/4/6 speculative drafts in the measured setting.

## Why it stopped

Closed as no-paper useful signal because the evidence is toy/synthetic and the broader self-speculative early-exit idea is already represented by LayerSkip; this run supports the mechanism but not a publication-grade claim.

## Recommended next action

Run a bounded GPT-2-small-class or miniature real-corpus confirmation with a KV-cache-aware verifier and compare against a final-loss-only control before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus early-exit self-speculative confirmation with cached verification
- Success threshold: Auxiliary early-exit model preserves final perplexity within 2 percent of control and achieves at least 1.5x tokens per verify cycle with measured end-to-end latency above greedy decoding on the same hardware.
- Stop condition: Stop if final perplexity regresses by more than 5 percent or gamma-4 draft acceptance remains below 25 percent after a calibrated training budget.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-draft-head-on-same-model-52b539aeb3d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

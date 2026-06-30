# VRAM-free speculative decoding via n-gram draft prediction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `vram-free-speculative-decoding-via-n-gram-draft-prediction-c44f5e2df640`
Run ID: `vram-free-speculative-decoding-via-n-gram-draft-prediction-c44f5e2df640-20260614T052842025150+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d4fd9fb89da0

## What looked useful

GPT-2-small accepted about 1.83-2.30 tokens per target forward for prompt-static n-grams and 1.94-2.26 for prompt-dynamic n-grams, with exact greedy output preserved in all 12 GPT-2-small prompts. This supports the mechanism but not a paper-ready broad claim.

## Boundaries and scale limits

Evidence is limited to GPT-2/distilgpt2, synthetic prompts, greedy decoding, short 40-token generations, and a non-production Python harness without KV-cache serving optimization. It does not validate 1B-8B+ instruction models, sampling, real RAG/summarization/ICL workloads, or production latency.

## Claim scope

In small GPT-2-class greedy decoding on six synthetic repetitive and six synthetic diverse prompts, a CPU-resident prompt/dynamic n-gram table can propose draft tokens that are accepted by target-model verification while preserving exact greedy output and using no second neural draft model in VRAM.

## Why it stopped

Small local evidence supports the mechanism, but close prior work exists and this run is synthetic/proxy-scale rather than publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should integrate the n-gram drafter into a KV-cache-aware verifier on realistic RAG or summarization prompts with a 1B-3B instruction model and compare against no speculation plus a published n-gram/retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware n-gram speculation on realistic RAG prompts
- Success threshold: Median accepted tokens per target forward >= 1.5 and median latency speedup >= 1.2x versus no speculation with exact greedy output preserved and GPU memory delta under 2 percent.
- Stop condition: Stop as negative if median accepted tokens per target forward is below 1.2 or if KV-cache overhead eliminates latency speedup on realistic prompts.

## Evidence references

- Artifact root: `<local-path>/projects/vram-free-speculative-decoding-via-n-gram-draft-prediction-c44f5e2df640`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

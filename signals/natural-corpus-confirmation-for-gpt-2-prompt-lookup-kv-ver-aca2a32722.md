# Natural-corpus confirmation for GPT-2 prompt-lookup KV verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-corpus-confirmation-for-gpt-2-prompt-lookup-kv-ver-aca2a32722`
Run ID: `natural-corpus-confirmation-for-gpt-2-prompt-lookup-kv-ver-aca2a32722-20260527T045533842509+0000`

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

- Parent run decision: N-gram draft speculative decoding for GPT-2 inference: enoch://control-plane/projects/n-gram-draft-speculative-decoding-for-gpt-2-inference-4b66d3d70382/runs/n-gram-draft-speculative-decoding-for-gpt-2-inference-4b66d3d70382-20260524T083503296929+0000
- Parent run decision: KV-cache n-gram draft verifier for GPT-2 prompt-lookup decoding: enoch://control-plane/projects/kv-cache-n-gram-draft-verifier-for-gpt-2-prompt-lookup-dec-d48a3be018/runs/kv-cache-n-gram-draft-verifier-for-gpt-2-prompt-lookup-dec-d48a3be018-20260524T155211433301+0000

## What looked useful

Prompt lookup produced drafts in 21.0% of 1,500 natural windows and achieved 0.301 accepted tokens per prompt versus 0.018 for random prompt continuations and 0.000 for shuffled lookup. Conditional on a lookup draft existing, mean accepted length was 1.435 tokens and first-token acceptance was 49.2%. A stricter min-3-gram ablation retained conditional quality but reduced availability to 7.7%.

## Boundaries and scale limits

Only gpt2, WikiText-103 validation, 384-token static prompts, draft length up to 8, greedy verification, and longest repeated suffix lookup were tested. End-to-end speculative decoding throughput, dynamic generation, longer contexts, larger models, other corpora, and production KV-cache overhead were not tested.

## Claim scope

GPT-2 small greedy verification on 1,500 WikiText-103 validation prompt windows shows natural prompt-lookup drafts are accepted more often than random prompt continuations and shuffled-token lookup controls, but only when repeated suffix matches are available.

## Why it stopped

Medium direct verification supports the mechanism but does not establish a paper-ready practical decoding result because absolute accepted-token yield is sparse and end-to-end speedup was not measured.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should measure end-to-end dynamic prompt-lookup speculative decoding throughput and acceptance on GPT-2 small across at least two natural corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 prompt-lookup speculative decoding on natural corpora
- Success threshold: At least 10% wall-clock tokens/sec improvement over vanilla greedy GPT-2 decoding on available-match subsets without regression on full-prompt averages, and prompt-lookup acceptance at least 5x random-draft acceptance across both corpora.
- Stop condition: Stop if dynamic prompt lookup gives less than 3% tokens/sec improvement on available-match subsets or if lookup availability remains below 5% on both corpora after reasonable n-gram/context ablations.

## Evidence references

- Artifact root: `<local-path>/projects/natural-corpus-confirmation-for-gpt-2-prompt-lookup-kv-ver-aca2a32722`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

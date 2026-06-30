# N-gram Prompt Lookup CPU Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-prompt-lookup-cpu-speculation-5d6358050b6b`
Run ID: `n-gram-prompt-lookup-cpu-speculation-5d6358050b6b-20260522T181006461088+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acbb5f2d3255

## What looked useful

Exact repeated-copy workloads achieved about 3.7-3.9 accepted tokens per attempt with sub-microsecond mean lookup; 5% mutated copies retained about 1.7-2.3 accepted tokens per attempt. Tiny Shakespeare natural text fell to 0.004-0.097 accepted tokens per attempt depending on n, making broad general-purpose CPU speculation unsupported.

## Boundaries and scale limits

No target LLM verifier, no production serving stack, no real RAG/chat traces, and workloads capped at 60000 word/punctuation tokens. The result supports mechanism-level triage, not end-to-end speedup claims.

## Claim scope

In bounded CPU-only exact-token benchmarks, rolling n-gram prompt lookup drafts are cheap and can produce multi-token accepted spans on exact or near-copy prompt continuations, but provide little useful acceptance on ordinary natural text.

## Why it stopped

Proxy benchmark closed the local question: the mechanism works for copy-heavy continuations but early-falsifies a broad natural-text prompt-lookup speculation claim; no paper-ready direct speedup evidence was produced.

## Recommended next action

Run one bounded deepen follow-up with a real small LLM verifier and target tokenizer on copy-heavy RAG/citation traces plus natural-chat controls; stop here for paper purposes because this run is proxy evidence, not end-to-end serving validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-verifier prompt lookup speculation on copy-heavy RAG traces
- Success threshold: On copy-heavy traces, reduce median generation latency or verifier passes by at least 15% versus no speculation without worsening output equivalence; on controls, show overhead is negligible or gated off.
- Stop condition: Stop if accepted tokens per attempt remain below 0.5 or end-to-end latency improves by less than 5% on copy-heavy traces after gating obvious lookup misses.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-prompt-lookup-cpu-speculation-5d6358050b6b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

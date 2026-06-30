# CPU N-Gram Speculative Decoding with Suffix Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-with-suffix-cache-c0c185c0a153`
Run ID: `cpu-n-gram-speculative-decoding-with-suffix-cache-c0c185c0a153-20260527T161120975328+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/529125218837

## What looked useful

CPU suffix-cache speculative proposals are cheap and useful on repetitive streams: synthetic logs reached 4.613x idealized target-call speedup and 78.3% target-call reduction. Natural prose was mixed: short 4-byte suffixes gave 1.406x to 1.631x idealized speedups, but 16-byte suffixes fell to 1.020x on tinyshakespeare and 1.058x on Alice, suggesting limited broad prose benefit without richer matching or model-aware proposal selection.

## Boundaries and scale limits

40,000 held-out byte tokens per corpus after a 100,000-byte cache warmup; single Python process; byte tokens rather than model-native tokens; no transformer verifier or sampling loop; no production serving traces.

## Claim scope

Dependency-free byte-token trace benchmark of a CPU n-gram suffix cache on tinyshakespeare, Alice in Wonderland, and synthetic log streams. The claim is limited to oracle-verified proposal hit rate, accepted draft length, target-call accounting, and CPU overhead, not real LLM wall-clock speedup.

## Why it stopped

Proxy trace evidence supports the mechanism for repetitive streams but does not provide direct LLM verifier or end-to-end wall-clock evidence required for a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a bounded GPT-2-small or similar real-decoder integration using model-native tokens and repeated-template prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-native suffix-cache speculative decoding on a small real decoder
- Success threshold: At least 15% end-to-end tokens/sec improvement and at least 25% target forward-pass reduction on repeated-template workloads, with identical greedy outputs and no more than 5% slowdown on natural-prose controls.
- Stop condition: Stop if target forward-pass reduction is under 10% or end-to-end throughput fails to improve on repeated-template prompts after controlling for cache overhead.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-with-suffix-cache-c0c185c0a153`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

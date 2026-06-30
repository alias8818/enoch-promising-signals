# CPU n-gram speculative cascade with fallback routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-cascade-with-fallback-routing-0e87f7149a3c`
Run ID: `cpu-n-gram-speculative-cascade-with-fallback-routing-0e87f7149a3c-20260522T110455865539+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/10b0868b9e9f

## What looked useful

The mechanism is cheap and behaves correctly, but coverage is the limiting factor: most real-text positions route to fallback because no confident n-gram draft exists. Naive n-gram speculation appears useful only for highly repetitive or cache-like workloads unless real model traces show substantially more repeated continuations.

## Boundaries and scale limits

No real LLM verifier, no GPU/CPU serving integration, regex tokenizer only, one public text corpus plus synthetic controls, 90k train tokens and 30k heldout tokens per grid dataset.

## Claim scope

In a local teacher-forced heldout-token proxy, a CPU n-gram speculative cascade with confidence-based fallback routing produces high-speed exact-match drafts but saves only about 6% fallback calls on heldout Tiny Shakespeare, while working perfectly on repeated text and not at all on random-token control.

## Why it stopped

Proxy evidence supports the mechanism but not a paper-ready or production-level claim; real-text fallback-call reduction was only 5.95% under heldout-stream evaluation.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a bounded real-LLM trace replay using the same tokenizer and explicit latency model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay CPU n-gram cascade on real LLM greedy output traces
- Success threshold: At least 15% fallback-call reduction on real LLM traces with CPU draft overhead below 5% of estimated target decode time and no correctness loss under exact verification.
- Stop condition: Stop if fallback-call reduction remains below 10% on real LLM traces or if CPU draft overhead erases the estimated latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-cascade-with-fallback-routing-0e87f7149a3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

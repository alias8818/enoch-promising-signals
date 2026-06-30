# Real-LM validation of persistent n-gram speculative decoding cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-lm-validation-of-persistent-n-gram-speculative-decodi-dee9c6db20`
Run ID: `real-lm-validation-of-persistent-n-gram-speculative-decodi-dee9c6db20-20260614T110711164916+0000`

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

- Parent run decision: PLD+ persistent cross-session n-gram cache spec decoding: enoch://control-plane/projects/pld-persistent-cross-session-n-gram-cache-spec-decoding-f42555210331/runs/pld-persistent-cross-session-n-gram-cache-spec-decoding-f42555210331-20260614T043041251219+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6dad8e1c9970

## What looked useful

Primary run: persistent cache matched greedy on 12/12 prompts and reduced verifier calls from 384 to 170 (55.7292%), versus 210 calls (45.3125%) for an ephemeral cache. Shuffled repeat: persistent used 171 calls (55.4688%) with 12/12 exact matches. This supports the mechanism but not paper readiness.

## Boundaries and scale limits

Only distilgpt2, 12 curated related prompts, 32 generated tokens per prompt, CPU PyTorch inference, and forward-call accounting were tested. No production KV-cache serving stack, larger model, held-out repeated-session corpus, memory-growth stress test, or adversarial domain-shift workload was tested.

## Claim scope

In a small controlled distilgpt2 greedy-decoding test over 12 related prompts, a persistent token n-gram cache used as a speculative draft source preserved exact greedy outputs and reduced verifier forward calls more than an ephemeral per-prompt cache.

## Why it stopped

Tier-1 direct validation succeeded as a useful mechanism signal, but the evidence is too small and systems-simplified for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up with a GPT-2-small-or-larger verifier, a held-out repeated-session text corpus, KV-cache-aware speculative verification, latency and memory metrics, and domain-shift controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache latency validation of persistent n-gram speculative decoding on repeated-session text
- Success threshold: Persistent cache must maintain 100% exact greedy-match equivalence, reduce p50 latency by at least 15%, reduce verifier forward calls by at least 25%, and outperform the ephemeral cache on latency or calls without unbounded cache growth.
- Stop condition: Stop as negative if exact greedy-match equivalence fails, persistent cache does not beat ephemeral cache on either latency or verifier calls, or cache memory growth is disproportionate to the observed speedup.

## Evidence references

- Artifact root: `<local-path>/projects/real-lm-validation-of-persistent-n-gram-speculative-decodi-dee9c6db20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

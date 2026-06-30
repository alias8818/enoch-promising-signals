# PLD+ persistent cross-session n-gram cache spec decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pld-persistent-cross-session-n-gram-cache-spec-decoding-f42555210331`
Run ID: `pld-persistent-cross-session-n-gram-cache-spec-decoding-f42555210331-20260614T043041251219+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6dad8e1c9970

## What looked useful

Main run reached 1.497x mean idealized target-step speedup and 33.209% target-step reduction for persistent cross-session cache versus 1.000x for no persistence; gains degraded under adversarial drift, 30% drift, and low-repeat controls.

## Boundaries and scale limits

No real language model, tokenizer, KV cache, batching, draft model latency, wall-clock serving, or output-quality validation was measured. Evidence is bounded to synthetic repeated sessions with exact-token oracle verification.

## Claim scope

Deterministic token-oracle simulation shows that a persistent cross-session 4-gram proposal cache can reduce idealized speculative-decoding target verification steps on repeated synthetic session streams.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only by a bounded simulator/proxy, not direct real-model speculative decoding evidence.

## Recommended next action

Run a bounded real-LM follow-up using a GPT-2-small-class model or similar, replayed prompts, and wall-clock latency/target-forward-pass metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM validation of persistent n-gram speculative decoding cache
- Success threshold: At least 1.20x median wall-clock decode speedup or at least 20% target-forward-pass reduction on warm repeated sessions versus both baselines, with exact output match for greedy decoding and less than 512 MB cache memory.
- Stop condition: Stop if warm persistent cache fails to beat session-local cache by 10% on target-forward-pass reduction or if cache memory/latency overhead erases wall-clock gains.

## Evidence references

- Artifact root: `<local-path>/projects/pld-persistent-cross-session-n-gram-cache-spec-decoding-f42555210331`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

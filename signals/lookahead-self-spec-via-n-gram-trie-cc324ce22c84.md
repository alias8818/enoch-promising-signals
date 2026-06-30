# Lookahead Self-Spec via N-Gram Trie

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lookahead-self-spec-via-n-gram-trie-cc324ce22c84`
Run ID: `lookahead-self-spec-via-n-gram-trie-cc324ce22c84-20260628T125221958547+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/01cf0d500512

## What looked useful

Trie lookahead produced speedup proxies from 1.60x to 4.99x in-domain for draft lengths 2 to 12, while the random-window control stayed near 1.02x; OOD Alice degraded but remained above random control.

## Boundaries and scale limits

No neural model verifier, no transformer KV-cache path, no measured GPU/serving latency, no stochastic speculative decoding acceptance, and only small public text corpora were tested.

## Claim scope

In a bounded CPU proxy using a deterministic 5-gram verifier trained on Tiny Shakespeare, an 8-context-token suffix trie drafts multi-token continuations that match verifier greedy output far above a random-window draft control on held-out Shakespeare and a small OOD Alice text condition.

## Why it stopped

No-paper useful signal from a controlled proxy experiment; evidence supports the mechanism but not a direct neural speculative-decoding claim.

## Recommended next action

Run a bounded neural-verifier follow-up with GPT-2-small-class exact speculative acceptance and wall-clock latency, stopping if trie acceptance or latency savings fall near the random/nearest-neighbor controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural verifier test for n-gram trie lookahead self-speculation
- Success threshold: At draft length 4 or 8, trie drafting achieves at least 1.25x measured latency improvement over one-token greedy decoding and at least 2x the accepted-token rate of random-window and nearest-neighbor controls on in-domain held-out text.
- Stop condition: Stop as negative if neural-verifier token acceptance is below 10%, measured latency improvement is below 1.10x, or trie overhead exceeds saved verifier time in two independent corpora.

## Evidence references

- Artifact root: `<local-path>/projects/lookahead-self-spec-via-n-gram-trie-cc324ce22c84`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

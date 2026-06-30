# Merkle Consensus Between Dual Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-consensus-between-dual-small-agents-9aa210b74225`
Run ID: `merkle-consensus-between-dual-small-agents-9aa210b74225-20260525T070122119389+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/111b44975757

## What looked useful

Merkle bisection is useful as a disagreement-localization primitive, not as a correctness guarantee. It reached 1.000 recall for detecting/localizing differing traces, but missed 10.4% of wrong-answer cases overall because shared wrong traces have identical roots. Communication was worse than full reveal for tiny 2-byte leaves overall but 0.328 of full reveal for 64-byte leaves.

## Boundaries and scale limits

No real language models, natural-language traces, adversarial behavior, or external task benchmarks were tested. The largest completed grid was 38,400 synthetic cases per leaf-size condition with up to 512 leaves.

## Claim scope

Synthetic dual-agent trace simulation shows SHA-256 Merkle commitments reliably detect and localize actual trace disagreements and can reduce communication for larger/text-like trace leaves, but they do not establish correctness when both agents share the same wrong trace.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic/proxy evidence: it supports the protocol mechanism for mismatch localization but does not validate correctness improvement between real small agents.

## Recommended next action

Run a bounded real-small-LM follow-up on verifiable intermediate-claim tasks, comparing Merkle trace consensus against final-answer voting, full transcript exchange, and an independent verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Merkle trace consensus on verifiable small-LM intermediate claims
- Success threshold: At least 95% recall for trace mismatches, at least 50% lower communication than full transcript exchange on text-like traces, and a statistically clear improvement over final-answer voting in detecting wrong answers not caused by shared identical errors.
- Stop condition: Stop if Merkle consensus fails to localize trace mismatches reliably, uses at least 80% of full transcript bytes on text-like traces, or does not improve wrong-answer detection over final-answer voting.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-consensus-between-dual-small-agents-9aa210b74225`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

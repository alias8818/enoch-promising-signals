# Home-Node Consensus Ledger for Catastrophic Error Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-node-consensus-ledger-for-catastrophic-error-reduction-118e95f06967`
Run ID: `home-node-consensus-ledger-for-catastrophic-error-reduction-118e95f06967-20260525T022701686342+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8993b96b9aa6

## What looked useful

Ledger memory produced a median 76.28% relative reduction in catastrophic acceptances versus majority consensus across the synthetic grid, but only 18.13% median reduction when failures were spread over 4000 families. Poisoned ledger entries added benign-rejection cost: about 0.876 percentage points at 1% poison and 4.37 percentage points at 5% poison.

## Boundaries and scale limits

No real LLM outputs, real home nodes, real network latency, incentive model, privacy model, or Byzantine ledger governance were tested. Results are limited to 27 synthetic scenarios with 7 verifier nodes, a 4-of-7 threshold, and 200000 tasks per policy/scenario.

## Claim scope

Synthetic verifier simulation: a shared ledger of confirmed catastrophic failure families can reduce repeated catastrophic acceptances versus stateless majority consensus when failure-family recurrence is high and poisoning is low.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal but not direct evidence for real-world home-node catastrophic-error reduction.

## Recommended next action

Run a bounded real-output replay using independent verifier prompts/models over a catastrophic-error benchmark, measuring recurrence, ledger hit rate, catastrophic acceptance, benign rejection, and poisoning sensitivity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-output replay test for consensus-ledger catastrophic-error screening
- Success threshold: Ledger consensus achieves at least 50% relative reduction in repeat catastrophic acceptances versus stateless majority while adding no more than 1 percentage point benign rejection at 1% poisoned ledger entries.
- Stop condition: Stop if benchmark recurrence is too low for ledger hits to cover at least 20% of catastrophic examples, or if benign rejection exceeds the 1 percentage point threshold at 1% poisoning.

## Evidence references

- Artifact root: `<local-path>/projects/home-node-consensus-ledger-for-catastrophic-error-reduction-118e95f06967`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

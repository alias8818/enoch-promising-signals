# Evidence Ledger for Small Agents: Falsifiable Claim-Counterexample Logging

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-small-agents-falsifiable-claim-counterexample-logging-27becd7a4712`
Run ID: `evidence-ledger-for-small-agents-falsifiable-claim-counterexample-logging-27becd7a4712-20260621T012802069880+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb2cc9445685

## What looked useful

Across 72,000 policy rows, ledger-guided counterexample search reduced false acceptances by a mean absolute 0.159 under 3x support-biased retrieval and 0.350 under 9x support-biased retrieval, but gave no benefit under unbiased retrieval; a no-ledger counterexample-search ablation closely matched ledger accuracy.

## Boundaries and scale limits

Synthetic attribute worlds only; no real LLM agents, no natural-language extraction, no real retrieval corpus, no adversarial semantic counterexamples, and no long-horizon memory or persistence stress test.

## Claim scope

In a deterministic synthetic universal-claim verification task, reserving part of an equal evidence-inspection budget for counterexample search reduced false acceptance when retrieval was biased toward confirming examples; durable ledger entries provided auditability but were not isolated as a causal accuracy improvement beyond the counterexample-search policy.

## Why it stopped

No-paper useful signal from a synthetic proxy: the main mechanism was counterexample budget allocation, not a demonstrated standalone benefit of ledger logging or persistence.

## Recommended next action

Run a bounded natural-language follow-up with small LLM agents where the ledger must persist extracted claims, retrieved supporting evidence, and explicit counterexamples across repeated verification tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language small-agent evidence ledger verification
- Success threshold: At least a 10 percentage point absolute false-acceptance reduction versus both confirmation baseline and no-ledger contradiction-search control, without more than a 5 percentage point true-acceptance loss on true claims.
- Stop condition: Stop if the ledger condition fails to beat the no-ledger contradiction-search control on false acceptance, or if ledger extraction/persistence errors exceed 10% of tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-agents-falsifiable-claim-counterexample-logging-27becd7a4712`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
